# Class definition of the elements

from schemdraw.elements import Element
from schemdraw.segments import Segment

class CustomNFet(Element):
    def __init__(self, linewidth=2, **kwargs):
        super().__init__(linewidth=linewidth, **kwargs)
        hh=0.9
        hw=0.5    
        g1_x=-hw+hw*0.8   
        g1_len=hh*1.1
        gap=hw*0.2
        g2_x=g1_x+gap
        g2_len=g1_len-0.15
        d_y=hh-hh*0.6
        arrow_w = 0.12
        arrow_l = 0.18
        db = 0.02   # Adjust thickness of MOS GATE
        
        # Gate lines
        self.segments.append(Segment([
            (g1_x, g1_len/2),
            (g1_x,-g1_len/2),
            (g1_x+db,-g1_len/2),
            (g1_x+db, g1_len/2),
            (g1_x, g1_len/2)], 
            fill='black'
        ))
        self.segments.append(Segment([
            (g2_x, g2_len/2),
            (g2_x,-g2_len/2),
            (g2_x+db,-g2_len/2),
            (g2_x+db, g2_len/2),
            (g2_x, g2_len/2)], 
            fill='black'
        )) 
        self.segments.append(Segment([
            (g2_x, 0),
            (hw,0)
        ]))
        # Source line with arrow
        self.segments.append(Segment([
            (g1_x,-d_y),
            (-hw, -d_y),
            (-hw, -hh)
        ]))
        self.segments.append(Segment([
            (-hw, -d_y),
            (-hw + arrow_l, -d_y + arrow_w/2),
            (-hw + arrow_l, -d_y - arrow_w/2),
            (-hw, -d_y)],
            fill='black'
        ))
        # Drain line (no arrow)
        self.segments.append(Segment([
            (g1_x,d_y),
            (-hw, d_y),
            (-hw, hh)
        ]))
        # Anchors
        self.anchors['gate'] = (hw, 0)
        self.anchors['source'] = (-hw,- hh)
        self.anchors['drain'] = (-hw, hh)
        self.anchors['center'] = (0, 0)


class CustomPFet(Element):
    def __init__(self, linewidth=2, **kwargs):
        super().__init__(linewidth=linewidth, **kwargs)
        hh=0.9
        hw=0.5    
        g1_x=-hw+hw*0.8   
        g1_len=hh*1.1
        gap=hw*0.2
        g2_x=g1_x+gap
        g2_len=g1_len-0.15
        d_y=hh-hh*0.6
        arrow_w = 0.12
        arrow_l = 0.18
        db = 0.02   # Adjust thickness of MOS GATE
        
        # Gate lines
        self.segments.append(Segment([
            (g1_x, g1_len/2),
            (g1_x,-g1_len/2),
            (g1_x+db,-g1_len/2),
            (g1_x+db, g1_len/2),
            (g1_x, g1_len/2)], 
            fill='black'
        ))
        self.segments.append(Segment([
            (g2_x, g2_len/2),
            (g2_x,-g2_len/2),
            (g2_x+db,-g2_len/2),
            (g2_x+db, g2_len/2),
            (g2_x, g2_len/2)], 
            fill='black'
        )) 
        self.segments.append(Segment([
            (g2_x, 0),
            (hw,0)
        ]))
        # Source line (no arrow)
        self.segments.append(Segment([
            (g1_x,-d_y),
            (-hw, -d_y),
            (-hw, -hh)
        ]))
        # Drain line (with arrow)
        self.segments.append(Segment([
            (g1_x,d_y),
            (-hw, d_y),
            (-hw, hh)
        ]))
        self.segments.append(Segment([
            (g1_x, d_y),
            (g1_x - arrow_l, d_y + arrow_w/2),
            (g1_x - arrow_l, d_y - arrow_w/2),
            (g1_x, d_y)],
            fill='black'
        ))
        # Anchors
        self.anchors['gate'] = (hw, 0)
        self.anchors['source'] = (-hw,- hh)
        self.anchors['drain'] = (-hw, hh)
        self.anchors['center'] = (0, 0)

