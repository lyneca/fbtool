# Facebook Messenger Tool
## A sexy monospaced way to do stuff quickly with Messenger


This project uses the awesome [facebook-chat-api](https://github.com/Schmavery/facebook-chat-api) built on node.js and the Electron web app framework to provide a sort of control panel for Messenger. Change colours without restriction, spam stuff (use responsibly), and send memes at the touch of a button.

App design fits right in with the atom editor, because, well, it's the same colour.
## Features:
- Log in and select thread
  - from a sidebar!
  - by ID
  - by searching a name of a 1-on-1 convo
- Change:
  - Thread colour (to an unrestricted hex colour!)
  - Nicknames
  - Emoji
- Send
  - A message `n` times
  - A random meme from [imgur](http://imgur.com/t/memes)
  - A random cute pic from [/r/aww](http://reddit.com/r/aww)

## Usage
1. Enter email/password and click `login` (or hit enter for the more keyboard friendly among us)
2. Select thread
  - Click on the thread on the all-new thread sidebar!
  - If a one-on-one thread (two people only):
    - Enter the name of the other person into the `thread:` field
    - Click `search friend`
  - If a group conversation
    - Enter the thread ID (visible in the URL of the chat: `https://www.messenger.com/t/[URL]`)
    - Click `load thread from ID`
3. Enjoy!


- Login may take 5-10 seconds.
- the `[emoji]` field must contain a valid single emoji.


### Running from source

Once you've cloned the source, cd to the root and
```bash
$ npm install && npm start
```

### Building
Project is built using [electron-packager](https://www.npmjs.com/package/electron-packager).
