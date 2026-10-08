# GemDeeds launch source

Full site and original artwork from the October 7 GemDeeds_GitHub_Upload package.

## Cloudflare Pages settings

- Repository: Cenzo14/gemdeeds
- Production branch: main
- Framework preset: None
- Build command: python3 build.py
- Build output directory: dist

The build unpacks core.zip, classic.zip and all seven art archives. Uploading the ZIPs alone does not produce a live website; configure the build command above.

The build preserves images, video, fonts, database connection and saved-data keys. It removes the old Netlify proxy dependency and serves Classic from this repository. The same Google font files and camera libraries load directly from their existing upstream CDNs.

Before connecting gemdeeds.com, test the Cloudflare preview: home artwork, world navigation, Classic, parent sign-in and family sync. Keep https://gemdeeds.com as the production origin to retain browser-local saves on existing devices. World Builder data is device-local; this migration does not add cross-device World Builder sync. Existing Classic data remains in the original Supabase project. Database health, backups and growth quotas still need verification.

gemdeeds.com currently points to paused Netlify hosting through Namecheap DNS. Connect the domain to Cloudflare Pages and update DNS only after the hosted preview passes. Preserve all mail/DNS records and leave Netlify available for rollback.
