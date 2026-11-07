# Profile assets source

- `architecture.html`: animates `architecture-still.png` (Sagar's own still) with a WebGL shader: camera push and parallax, flowing waterfalls, light running along highlights, crystal pulse and scan ring, cloud churn, embers, and a name shimmer (10 s loop). Render with `node capx.js architecture.html f fps:15:10 2172 724` with 724 as the height argument, then `ffmpeg -framerate 15 -i f/%03d.png -vf format=yuv420p -c:v libsvtav1 -crf 30 -preset 5 -g 150 -f avif banner.avif`. `banner.webp` is a 1000 px fallback for browsers without AVIF.

- `gauntlet.html`: the three.js scene behind `assets/banner.webp`. An armored data gauntlet snaps, then the holographic data world builds and plays out (12 s). Serve this folder over HTTP with `three@0.170.0` in `node_modules`, run `node capx.js gauntlet.html f fps:15:12 3200`, then
  `ffmpeg -framerate 15 -i f/%03d.png -vf scale=2400:600:flags=lanczos -c:v libwebp -q:v 75 -compression_level 6 -loop 0 banner.webp` (renders at 3200×800, downsampled to 2400×600 for crisp edges under 10 MB).

- `hero.html`: the previous ray-traced data-hero banner scene, with HTML overlays for the headline and HUD panels. Serve this folder over HTTP with `three@0.170.0` installed in `node_modules`, then run `node cap.js 0 f x 15` to render 150 frames (10 s at 15 fps). Turn the frames into the banner with
  `ffmpeg -framerate 15 -i f/%03d.png -c:v libwebp -q:v 72 -compression_level 6 -loop 0 banner.webp`.
- `gen_svgs.py`: writes every themed SVG in `assets/` (section headers, project cards, lifecycle, principles, toolbox, footer). Run `python3 gen_svgs.py ../assets`.
