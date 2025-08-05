from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from channels.db import database_sync_to_async


class ChatConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name=None
        self.user_name=None
    async def connect(self):
        if not self.scope["user"]:
            return await self.close()
        await self.accept()
        self.room_name = self.scope["url_route"]["kwargs"]["room"]
        self.user_name = await self.get_profile_name()
        print(self.user_name, self.room_name)


    @database_sync_to_async
    def get_profile_name(self):
        user=self.scope["user"]
        return user.profile.name