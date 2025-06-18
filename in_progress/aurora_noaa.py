"""API Wrapper for NOAA Aurora 30 Minute Forecast."""

import asyncio
import json
import logging
import time
from tkinter import *

import aiohttp
from aiohttp import ClientError

APIUrl = "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"

_LOGGER = logging.getLogger("aurora")
_LOGGER.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
_LOGGER.addHandler(handler)


class AuroraForecast:
    forecast_dict = {}
    last_update_time = None
    lock = asyncio.Lock()

    def __init__(self, session: aiohttp.ClientSession = None):
        self.retry = 5

        if session:
            self._session = session
        else:
            self._session = aiohttp.ClientSession()

    async def close(self):
        await self._session.close()

    async def get_forecast_data(self, latitude: float, longitude: float):
        await AuroraForecast.lock.acquire()

        try:
            if longitude < 0:
                longitude = 360 + longitude

            if AuroraForecast.last_update_time is None or (
                time.monotonic() - AuroraForecast.last_update_time > 5 * 60
            ) or not AuroraForecast.forecast_dict:
                AuroraForecast.forecast_dict = {}

                _LOGGER.debug("Fetching forecast data from NOAA")
                try:
                    async with self._session.get(APIUrl) as resp:
                        resp.raise_for_status()
                        forecast_data = await resp.json()

                        for forecast_item in forecast_data["coordinates"]:
                            if forecast_item[2] > 0:
                                AuroraForecast.forecast_dict[
                                    (round(forecast_item[0]), round(forecast_item[1]))
                                ] = forecast_item[2]

                        AuroraForecast.last_update_time = time.monotonic()
                        _LOGGER.debug("Successfully fetched forecast data from NOAA")

                except ClientError as error:
                    _LOGGER.error("Error fetching forecast from NOAA: %s", error)
                except json.JSONDecodeError as error:
                    _LOGGER.error("Error decoding JSON from NOAA response: %s", error)
                except KeyError:
                    _LOGGER.error("Unexpected data structure from NOAA API. Missing 'coordinates' key.")

            probability = AuroraForecast.forecast_dict.get(
                (round(longitude), round(latitude)), 0
            )
            _LOGGER.debug(
                "Forecast probability: %s at (long, lat) = (%s, %s)",
                probability,
                round(longitude),
                round(latitude),
            )
            return probability

        finally:
            AuroraForecast.lock.release()

async def main():
    print("Hello Dudes and Dudettes")
    
    aurora_predicter = Tk()
    aurora_predicter.title("Aurora Forecaster")
    aurora_predicter.geometry('500x300')
    aurora_predicter.resizable(True, True)
    aurora_predicter.config(bg="#F0F0F0")

    main_frame = Frame(aurora_predicter, bg="#F0F0F0", padx=20, pady=20)
    main_frame.pack(expand=True, anchor="center")

    title_label = Label(main_frame, text="Aurora Forecast", font=("Helvetica Neue", 24, "bold"), bg="#F0F0F0", fg="#333")
    title_label.pack(pady=10)

    latitude_entry = Entry(aurora_predicter)
    latitude_entry.pack()

    def get_latitude():
        text = latitude_entry.get()
        print("Latitude: ", text)
        text = latitude_input

    latitude_button = Button(aurora_predicter, text="Get Latitude", command = get_latitude)
    latitude_button.pack()

    longitude_entry = Entry(aurora_predicter)
    longitude_entry.pack()

    def get_longitude():
        text_lo = longitude_entry.get()
        print("Longitude: ", text_lo)
        text_lo = longitude_input

    longitude_button = Button(aurora_predicter, text="Get longitude", command = get_longitude)
    longitude_button.pack()

    latitude_input = 44.2272
    longitude_input = 71.7479

    aurora_service = AuroraForecast()
    
    boolboolboolbool = False

    def update_long_lat():
        longitude_input = longitude_entry.get()
        latitude_input = latitude_entry.get()
        boolboolboolbool = True

    async def get_forecast_conditionally(boolboolboolbool, latitude_input, longitude_input):
        if boolboolboolbool:
            return await aurora_service.get_forecast_data(latitude=latitude_input, longitude=longitude_input)
            percent_label.config(f"Forecast Chance: {forecast}%", main_frame, font=("Helvetica Neue", 18), bg="#F0F0F0", fg="#555")
            status_label.config(text=f"For Lat: {latitude_input:.2f}, Long: {longitude_input:.2f}")
        else:
            return None  

    #forecast = await get_forecast_conditionally(boolboolboolbool, latitude_input, longitude_input)

    update_long_lat_button = Button(aurora_predicter, text = "Update Long&Lat", command = update_long_lat)
    update_long_lat_button.pack()
    
    forecast = await aurora_service.get_forecast_data(latitude=latitude_input, longitude=longitude_input)
    
    percent_text = f"Forecast Chance: {forecast}%"
    percent_label = Label(main_frame, text=percent_text, font=("Helvetica Neue", 18), bg="#F0F0F0", fg="#555")
    percent_label.pack(pady=20)

    status_label = Label(main_frame, text="Fetching data...", font=("Helvetica Neue", 12), bg="#F0F0F0", fg="#888")
    status_label.pack(pady=5)
    
    status_label.config(text=f"For Lat: {latitude_input:.2f}, Long: {longitude_input:.2f}")

    print(f"Forecast Chance: {forecast}% for Lat: {latitude_input}, Long: {longitude_input}")

    await aurora_service.close()

    aurora_predicter.mainloop()

if __name__ == '__main__':
    asyncio.run(main())
