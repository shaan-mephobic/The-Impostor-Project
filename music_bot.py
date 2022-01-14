import asyncio
import functools
import itertools
import math
import random
import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
import time
import subprocess
import sys
import requests

client = commands.Bot('>', description='THE IMPOSTOR PROJECT COMMANDS')

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def yomama(self, ctx):
        ''': Return a yomama joke'''
        await ctx.send(requests.get("https://yomomma-api.herokuapp.com/jokes").json()['joke'])
        
    @commands.command()
    async def joke(self, ctx):
        ''': Return a joke'''
        await ctx.send(requests.get("https://geek-jokes.sameerkumar.website/api?format=json").json()['joke'])
        
    @commands.command()
    async def chuck(self, ctx):
        ''': Return a Chuck Norris joke'''
        await ctx.send(requests.get("https://api.chucknorris.io/jokes/random").json()['value'])

    @commands.command()
    async def stoicism(self, ctx):
        ''': Return a Stoicism quote'''
        data = requests.get("https://api.themotivate365.com/stoic-quote").json()['data']
        await ctx.send(data['quote']+"\n~"+data['author'])
        
    @commands.command()
    async def quote(self, ctx):
        ''': Return a quote'''
        data = requests.get("https://inspiration.goprogram.ai/").json()
        await ctx.send(data['quote']+"\n~"+data['author'])
        
    @commands.command()
    async def randomidea(self, ctx):
        ''': Generate random ideas'''
        data = requests.get("https://itsthisforthat.com/api.php?json").json()
        await ctx.send(data['this']+" "+data['that'])

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        ''': Clears The Messages Eg: >Clear 69.(only admins)'''
        await ctx.channel.purge(limit= amount + 1)

    @commands.command()
    async def stfu(self, ctx): 
        ''': Says A Random Person In VC To STFU'''
        vc = ctx.author.voice.channel
        thels=[]
        for member in vc.members:
            thels.append(str(member))
        membe=random.choice(thels)
        await ctx.send("Yo "+membe+" Why can't you just Shut the Fuck Up!")

    @commands.command()
    async def ping(self, ctx):
        ''': Find The Latency Of The Bot'''
        await ctx.send(f'Ping is {round(client.latency * 1000)}ms')
                    
    @commands.command()
    async def whoissus(self, ctx):
        ''': Reveals The Imposter...(NOT REALLY)'''
        vc = ctx.author.voice.channel
        thels=[]
        for member in vc.members:
            thels.append(str(member))
        mem=random.choice(thels)
        await ctx.send(mem +" kinda looks sus, don't you think?")
        
    @commands.command()
    async def roast(self, ctx):
        ''': Roast You  '''
        listofroast=["YOUR FAMILY TREE MUST BE A CACTUS BECAUSE EVERYBODY ON IT IS A PRICK.","YO MAMA'S LIKE THE PANAMA CANAL, VESSELS FULL OF SEAMEN PASS THROUGH HER EVERYDAY.","I HEARD THAT YOUR BROTHER WAS AN ONLY CHILD.","I'D CALL YOU A CUNT, BUT YOU LACK BOTH THE DEPTH AND THE WARMTH.","THE LAST TIME I SAW A FACE LIKE YOURS I FED IT A BANANA.","WHY DON'T YOU SLIP INTO SOMETHING MORE COMFORTABLE -- LIKE A COMA.","YOUR BIRTH CERTIFICATE IS AN APOLOGY LETTER FROM THE CONDOM FACTORY.","YOU'RE SO FAT THE ONLY LETTERS OF THE ALPHABET YOU KNOW ARE KFC.","WITH A FACE LIKE YOURS, I'D WISH I WAS BLIND.","GO APOLOGIZE TO YOUR MOTHER FOR NOT BEING A STILLBORN.","YOUR DICK IS SO SMALL, YOU BOUGHT A KEYCHAIN FLESHLIGHT.","EXCELLENT TIME TO BECOME A MISSING PERSON.","HAVE YOU CONSIDERED SUING YOUR BRAINS FOR NONSUPPORT?","IF YOU WERE ANY STUPIDER, I WOULD HAVE TO WATER YOU TWICE A WEEK.","OH MY GOD, LOOK AT YOU. WAS ANYONE ELSE HURT IN THE ACCIDENT?","CALLING YOU STUPID WOULD BE AN INSULT TO STUPID PEOPLE.","IF YOU REALLY WANT TO KNOW ABOUT MISTAKES, YOU SHOULD ASK YOUR PARENTS.","IF YOU WANT PUSSY JUICE ROLLING DOWN YOUR FACE RN, BETTER START CRYING.","SORRY I DON'T REMEMBER YOU, MOSTLY BECAUSE I DON'T LOOK DOWN BEFORE FLUSHING THE TOILET.","You’re the reason God created the middle finger.","Don’t you get tired of putting make up on two faces every morning?","It’s a shame you can’t Photoshop your personality.","Jealousy is a disease. Get well soon, bitch!","Sorry, sarcasm falls out of my mouth like bullshit falls out of yours.","You have more faces than Mount Rushmore.","Yes, I am a bitch — just not yours.","You should wear a condom on your head. If you’re going to be a dick, you might as well dress like one. ","Being a bitch is a tough job but someone has to do it. ","My middle finger gets a boner every time I see you. ","You’re so real. A real ass.","If I had a face like yours I’d sue my parents.","Whoever told you to be yourself gave you really bad advice.","I didn’t change. I grew up. You should try it sometime.","I thought I had the flu, but then I realized your face makes me sick to my stomach.","I’m jealous of people who don’t know you.","I Wish Shaan could make an app that can make you disappear?","I’d smack you, but that would be animal abuse.","Hey, I found your nose, it’s in my business again!","You’re like a plunger. You like to bring up old shit. ","I hide behind sarcasm because telling you to go fuck yourself is rude in most social situations.","I’d explain it to you but I left my English-to-Dumbass Dictionary at home."]
        roater=random.choice(listofroast)
        await ctx.send(roater)

    @commands.command()
    async def suggestamovie(self, ctx):
        ''': Suggest Handpicked Movies For You To Watch '''
        listofmovies=["INTO THE WILD","LUCY","AMERICAN PIE TRIOLOGY","SE7EN","2001: A SPACE ODYSSEY","ALL NOLAN MOVIES FFS","LOVE & OTHER DRUGS","MURDER ON THE ORIENT EXPRESS","JOHN WICK ALL FUCKING PARTS","CATCH ME IF YOU CAN","READY PLAYER ONE","COMMIT SUICIDE IF YOU HAVEN'T WATCHED SHREK","ZOMBIELAND","SUPERBAD","TWO NIGHT STAND","SHAUN OF THE DEAD","CRAZY STUPID LOVE","500 DAYS OF SUMMER","SILVER LININGS PLAYBOOK","PASSENGER"]
        siwe=random.choice(listofmovies)
        await ctx.send(siwe)

client.add_cog(Commands(client))

class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': False,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    # FFMPEG_OPTIONS = {
    #     'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    #     'options': '-vn',
    # }
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)
    # YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'}
    

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 1.0
        self.skip_votes = set()

        self.audio_player = bot.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                try:
                    async with timeout(600):  # 10 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.bot.loop.create_task(self.stop(self))
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self,ctx: commands.Context):
        self.songs.clear()

        if ctx.voice_state.is_playing:
            await ctx.voice_state.stop()


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        """: Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='summon')
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """: Summons the bot to a voice channel.
        If no channel was specified, it joins your channel.
        """

        if channel and ctx.author.voice:
            raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='leave', aliases=['disconnect'])
    async def _disconnect(self, ctx):
        """: Leaves the voice channel, if currently in one."""
        if ctx.guild.voice_client and ctx.guild.voice_client.channel:
            await ctx.invoke(client.get_command('stop'))
            await ctx.guild.voice_client.disconnect()
        else:
            raise commands.CommandError("Not in a voice channel.")


    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """: Sets the volume of the player."""

        if ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        """: Displays which song is being played now."""

        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause')
    async def _pause(self, ctx: commands.Context):
        """: Pauses the playing song."""

        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='resume')
    async def _resume(self, ctx: commands.Context):
        """: Resumes the paused song."""
        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='stop')
    async def _stop(self, ctx: commands.Context):
        """: Stops playing the song and clears the queue."""

        ctx.voice_state.songs.clear()

        if ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')

    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        """: Vote to skip a song.
        """
        ctx.voice_state.skip()

    @commands.command(name='restart')
    @commands.has_permissions(administrator=True)
    async def _rest(self, ctx: commands.Context):
        ''': restarts the Bot(only-Admins)'''
        await ctx.send("Restarted")
        await client.logout()
        subprocess.call([sys.executable, "music_bot.py"])
        await ctx.send("I am Up and Runnin'")

    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        """: Shows the player's queue.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """: Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        """: Removes the song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @commands.command(name='loop')
    async def _loop(self, ctx: commands.Context):
        """: Loops the current song.
        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')

    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        """: Plays a song.
        If there are songs in the queue, this will be queued until the
        other songs finished playing.
        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search)
            except YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                song = Song(source)
                await ctx.voice_state.songs.put(song)
                await ctx.send('Enqueued {}'.format(str(source)))
    
    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')

    @commands.command(name='game')
    async def _game(self, ctx: commands.Context):
        ''': mutes all of them (Beware of annoying kids)'''
        vc = ctx.author.voice.channel
        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except:
            pass
        for member in vc.members:
            print(member)
            impostor=str(member)
            print(impostor)
            if (impostor !="Rythm#3722" and impostor!="The-Impostor-Project#4105") and impostor != "The-Imposter-Kid#2083":
                await member.edit(mute=True) 
            else:
                print("haha jokes on you")

    @commands.command(name='done')
    async def _done(self, ctx: commands.Context):
        ''': Unmutes everyone in VC and pauses the music'''
        vc = ctx.author.voice.channel
        try:
            channel = ctx.author.voice.channel
            await channel.disconnect()
            await client.logout()
            subprocess.call([sys.executable, "music_bot.py"])
        except:
            pass
        for member in vc.members:
            await member.edit(mute=False)
        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='done!')
    async def _don(self, ctx: commands.Context):
        ''': Unmutes everyone in VC without pausing the music'''
        vc = ctx.author.voice.channel
        try:
            channel = ctx.author.voice.channel
            await channel.disconnect()
            await client.logout()
            subprocess.call([sys.executable, "music_bot.py"])
        except:
            pass
        for member in vc.members:
            await member.edit(mute=False)
    
    @commands.command(name='meet')
    async def _meet(self, ctx: commands.Context, ammount: int ):
        ''': Unmutes Everyone And Pauses The Music So Everyone Can Talk And Mutes And Resumes The Music After The Time Specified'''
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=False)
        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
        await asyncio.sleep(ammount + 5)

        ctx.voice_state.voice.resume()

        for member in vc.members:
            print(member)
            impostor=str(member)
            print(impostor)
            if (impostor !="Rythm#3722" and impostor!="The-Impostor-Project#4105") and impostor != "The-Imposter-Kid#2083":
                await member.edit(mute=True)

client.add_cog(Music(client))

@client.event
async def on_ready():
    print("Up And Runnin'!")

client.run('TOKEN')
