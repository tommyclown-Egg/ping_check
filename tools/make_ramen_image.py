import sys
from PIL import Image, ImageDraw, ImageFont
src,out,shop,station,access=sys.argv[1:6]
FONT="/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
im=Image.open(src).convert("RGBA"); W,H=im.size
YEL=(255,226,0); WHT=(255,255,255); DARK=(25,8,0); RED=(214,28,28)
def text(xy,t,size,fill,anchor="la"):
    lay=Image.new("RGBA",im.size,(0,0,0,0)); d=ImageDraw.Draw(lay)
    f=ImageFont.truetype(FONT,size); x,y=xy
    o=max(3,size//22); b=max(1,size//75); sh=max(4,size//28)
    d.text((x+sh,y+sh),t,font=f,fill=(0,0,0,150),stroke_width=o,stroke_fill=(0,0,0,150),anchor=anchor)
    d.text((x,y),t,font=f,fill=DARK,stroke_width=o,stroke_fill=DARK,anchor=anchor)
    d.text((x,y),t,font=f,fill=fill,stroke_width=b,stroke_fill=fill,anchor=anchor)
    im.alpha_composite(lay)
# station
text((70,60),station,300,YEL)
# access vertical
tr=str.maketrans("0123456789","０１２３４５６７８９")
size=165; y=80; x=W-50-size//2
for c in access.translate(tr):
    text((x,y),c,size,WHT,"ma"); y+=int(size*1.12)
# shop name on red plate
size=270
f=ImageFont.truetype(FONT,size); bb=f.getbbox(shop)
tw=bb[2]-bb[0]; pw,ph=tw+160,size+90
px=(W-pw)//2; py=H-ph-60
lay=Image.new("RGBA",im.size,(0,0,0,0)); d=ImageDraw.Draw(lay)
d.rounded_rectangle((px,py,px+pw,py+ph),radius=50,fill=RED+(235,),outline=WHT+(255,),width=8)
im.alpha_composite(lay)
text((W//2,py+ph//2+size//2-25),shop,size,YEL,"ms")
im.convert("RGB").save(out,quality=95)
