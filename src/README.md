# Profile assets source

- `hero.html`: the ray-traced (GLSL through three.js) data-hero scene behind `assets/banner.webp`, with HTML overlays for the headline and HUD panels. Serve this folder over HTTP with `three@0.170.0` installed in `node_modules`, then run `node cap.js 0 f x 15` to render 150 frames (10 s at 15 fps). Turn the frames into the banner with
  `ffmpeg -framerate 15 -i f/%03d.png -c:v libwebp -q:v 72 -compression_level 6 -loop 0 banner.webp`.
- `gen_svgs.py`: writes every themed SVG in `assets/` (section headers, project cards, lifecycle, principles, toolbox, footer). Run `python3 gen_svgs.py ../assets`.
