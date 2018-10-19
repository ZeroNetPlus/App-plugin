# AppPlugin currently is not too automated, then you need to do some manual work

If you want to turn an zite into an WWW site or mobile/desktop app, then you will need to create a new ZeroNet installation. And on this brand new installation, your zite will be the main zite, acting like ZeroHello. Only this zite is enabled, and users can't download other zites, but can download new user data/optional files from the main zite (that is the site/app). But as master of this ZeroNet installation, you can manually add merged zites/hubs and ID/certificate providers, that are needed for main zite.

Follow all those instructions while your new ZeroNet installation isn't running.

## Turn on Multiuser plugin

1. Go to [your-zeronet-new-installation-path]\core\plugins
2. Find disabled-Multiuser folder
3. Rename it by removing the disabled- prefix

### [Optional] Turn your app into a "super peer" (tracker)
If you want to help ZeroNet, you can be a network tracker.
You need to have an fixed IPv4/IPv6 address or use CJDNS address.
1. Go to [your-zeronet-new-installation-path]\core\plugins
2. Find disabled-Bootstrapper folder
3. Rename it by removing the disabled- prefix

## Choose your main zite and turn it into the start page (replacing ZeroHello)