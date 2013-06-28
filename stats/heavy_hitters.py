#!/usr/bin/env python

class HeavyHitters:
    def __init__(self, N):
        self.N = N
        self.c_to_wc    = {}
        self.wc         = []

    def update(self, c, v):
        try:
            wc = self.c_to_wc.pop(c)
            self.wc.remove(wc)
            wc2 = (wc[0]+v,c)
        except KeyError:
            if len(self.wc) < self.N:
                wc2 = (v,c)
            else:
                wc = self.wc.pop(0)
                self.c_to_wc.pop(wc[1])
                wc2 = (wc[0]+v, c)

        self.c_to_wc[c] = wc2
        self.wc.append(wc2)
        self.wc.sort()

    def summery(self):
        return self.wc

