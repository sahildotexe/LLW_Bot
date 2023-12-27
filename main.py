from fastapi import FastAPI, HTTPException

from telethon.sync import TelegramClient
from telethon.tl.types import InputUserSelf

app = FastAPI()

api_id = '19978833'
api_hash = 'dc303aace620ee2e861adbca79742072'

@app.get("/get_user_id/{phone_number}")
async def get_user_id(phone_number: str):
    try:
        client = TelegramClient('session_name', api_id, api_hash)

        await client.start(bot_token='6913651280:AAHqctuJXTSuQPBiej2tKJ8-6DJwGzdR1CQ')

        entity = await client.get_input_entity(phone_number)
        if entity:
            user_id = entity.user_id
            return {"user_id": user_id}
        else:
            raise HTTPException(status_code=404, detail=f"Could not find user with phone number {phone_number}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app using UVicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
