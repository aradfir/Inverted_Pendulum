# -*- coding: utf-8 -*-

# python imports
from math import degrees
import numpy as np




class FuzzyControllerArad:
    dt = 0.1

    def __init__(self):
        pass

    def interpolate_line(self, x1, y1, x2, y2, x):
        slope = (y2 - y1) / float(x2 - x1)
        y = y1 + slope * (x - x1)
        return y

    def _make_input(self, world):
        return dict(
            cp=world.x,
            cv=world.v,
            pa=degrees(world.theta),
            pv=degrees(world.omega)
        )

    def _make_output(self):
        return dict(
            force=0.
        )

    def get_membership_value(self, x_start, x_end, x_peak, y_start, y_end, y_peak, x):
        if x < x_start:
            return y_start
        elif x > x_end:
            return y_end
        elif x == x_peak:
            return y_peak
        elif x < x_peak:
            return self.interpolate_line(x_start, y_start, x_peak, y_peak, x)
        else:
            return self.interpolate_line(x_peak, y_peak, x_end, y_end, x)

    # fuzzification of two parameters
    def pv_cw_fast(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = -200, 1, -200, 1, -100, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pv_cw_slow(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = -200, 0, -100, 1, 0, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pv_stop(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = -100, 0, 0, 1, 100, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pv_ccw_slow(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 0, 0, 100, 1, 200, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pv_ccw_fast(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 100, 0, 200, 1, 200.1, 1
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_up_more_right(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 0, 0, 30, 1, 60, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_up_right(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 30, 0, 60, 1, 90, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_up(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 60, 0, 90, 1, 120, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_up_left(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 90, 0, 120, 1, 150, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_up_more_left(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 120, 0, 150, 1, 180, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_down_more_left(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 180, 0, 210, 1, 240, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_down_left(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 210, 0, 240, 1, 270, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_down(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 240, 0, 270, 1, 300, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_down_right(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 270, 0, 300, 1, 330, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def pa_down_more_right(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 300, 0, 330, 1, 360, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    # force membership, used for defuzzification
    def force_left_fast(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = -100, 0, -80, 1, -60, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def force_left_slow(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = -80, 0, -60, 1, 0, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def force_stop(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = -60, 0, 0, 1, 60, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def force_right_slow(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 0, 0, 60, 1, 80, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def force_right_fast(self, x):
        x_start, y_start, x_peak, y_peak, x_end, y_end = 60, 0, 80, 1, 100, 0
        return self.get_membership_value(x_start, x_end, x_peak, y_start, y_end, y_peak, x)

    def inference(self, pa, pv):
        #if pa < 0:
        #    pa = 360+ pa
        force_limits = dict()
        force_limits['left_fast'] = list()
        force_limits['left_slow'] = list()
        force_limits['stop'] = list()
        force_limits['right_fast'] = list()
        force_limits['right_slow'] = list()

        # 0
        force_limits['stop'].append(max(
            min(self.pa_up(pa), self.pv_stop(pv)), min(self.pa_up_right(pa), self.pv_ccw_slow(pv)),
            min(self.pa_up_left(pa), self.pv_cw_slow(pv))
        ))

        # 1
        force_limits['right_fast'].append(min(self.pa_up_more_right(pa), self.pv_ccw_slow(pv)))
        # 2
        force_limits['right_fast'].append(min(self.pa_up_more_right(pa), self.pv_cw_slow(pv)))
        # 3
        force_limits['left_fast'].append(min(self.pa_up_more_left(pa), self.pv_cw_slow(pv)))
        # 4
        force_limits['left_fast'].append(min(self.pa_up_more_left(pa), self.pv_ccw_slow(pv)))
        # 5
        force_limits['left_slow'].append(min(self.pa_up_more_right(pa), self.pv_ccw_fast(pv)))
        # 6
        force_limits['right_fast'].append(min(self.pa_up_more_right(pa), self.pv_cw_fast(pv)))
        # 7
        force_limits['right_slow'].append(min(self.pa_up_more_left(pa), self.pv_cw_fast(pv)))
        # 8
        force_limits['left_fast'].append(min(self.pa_up_more_left(pa), self.pv_ccw_fast(pv)))
        # 9
        force_limits['right_fast'].append(min(self.pa_down_more_right(pa), self.pv_ccw_slow(pv)))
        # 10
        force_limits['stop'].append(min(self.pa_down_more_right(pa), self.pv_cw_slow(pv)))
        # 11
        force_limits['left_fast'].append(min(self.pa_down_more_left(pa), self.pv_cw_slow(pv)))
        # 12
        force_limits['stop'].append(min(self.pa_down_more_left(pa), self.pv_ccw_slow(pv)))
        # 13
        force_limits['stop'].append(min(self.pa_down_more_right(pa), self.pv_ccw_fast(pv)))
        # 14
        force_limits['stop'].append(min(self.pa_down_more_right(pa), self.pv_cw_fast(pv)))
        # 15
        force_limits['stop'].append(min(self.pa_down_more_left(pa), self.pv_cw_fast(pv)))
        # 16
        force_limits['stop'].append(min(self.pa_down_more_left(pa), self.pv_ccw_fast(pv)))
        # 17
        force_limits['right_fast'].append(min(self.pa_down_right(pa), self.pv_ccw_slow(pv)))
        # 18
        force_limits['right_fast'].append(min(self.pa_down_right(pa), self.pv_cw_slow(pv)))
        # 19
        force_limits['left_fast'].append(min(self.pa_down_left(pa), self.pv_cw_slow(pv)))
        # 20
        force_limits['left_fast'].append(min(self.pa_down_left(pa), self.pv_ccw_slow(pv)))
        # 21
        force_limits['stop'].append(min(self.pa_down_right(pa), self.pv_ccw_fast(pv)))
        # 22
        force_limits['right_slow'].append(min(self.pa_down_right(pa), self.pv_cw_fast(pv)))
        # 23
        force_limits['stop'].append(min(self.pa_down_left(pa), self.pv_cw_fast(pv)))
        # 24
        force_limits['left_slow'].append(min(self.pa_down_left(pa), self.pv_ccw_fast(pv)))
        # 25
        force_limits['right_slow'].append(min(self.pa_up_right(pa), self.pv_ccw_slow(pv)))
        # 26
        force_limits['right_fast'].append(min(self.pa_up_right(pa), self.pv_cw_slow(pv)))
        # 27
        force_limits['right_fast'].append(min(self.pa_up_right(pa), self.pv_stop(pv)))
        # 28
        force_limits['left_slow'].append(min(self.pa_up_left(pa), self.pv_cw_slow(pv)))
        # 29
        force_limits['left_fast'].append(min(self.pa_up_left(pa), self.pv_ccw_slow(pv)))
        # 30
        force_limits['left_fast'].append(min(self.pa_up_left(pa), self.pv_stop(pv)))
        # 31
        force_limits['left_fast'].append(min(self.pa_up_right(pa), self.pv_ccw_fast(pv)))
        # 32
        force_limits['right_fast'].append(min(self.pa_up_right(pa), self.pv_cw_fast(pv)))
        # 33
        force_limits['right_fast'].append(min(self.pa_up_left(pa), self.pv_cw_fast(pv)))
        # 34
        force_limits['left_fast'].append(min(self.pa_up_left(pa), self.pv_ccw_fast(pv)))
        # 35
        force_limits['right_fast'].append(min(self.pa_down(pa), self.pv_stop(pv)))
        # 36
        force_limits['stop'].append(min(self.pa_down(pa), self.pv_cw_fast(pv)))
        # 37
        force_limits['stop'].append(min(self.pa_down(pa), self.pv_ccw_fast(pv)))
        # 38
        force_limits['left_slow'].append(min(self.pa_up(pa), self.pv_ccw_slow(pv)))
        # 39
        force_limits['left_fast'].append(min(self.pa_up(pa), self.pv_ccw_fast(pv)))
        # 40
        force_limits['right_slow'].append(min(self.pa_up(pa), self.pv_cw_slow(pv)))
        # 41
        force_limits['right_fast'].append(min(self.pa_up(pa), self.pv_cw_fast(pv)))
        # 42
        force_limits['stop'].append(min(self.pa_up(pa), self.pv_stop(pv)))

        forces_final=dict()
        forces_final['left_fast'] = max(force_limits['left_fast'])
        forces_final['right_fast'] = max(force_limits['right_fast'])
        forces_final['left_slow'] = max(force_limits['left_slow'])
        forces_final['right_slow'] = max(force_limits['right_slow'])
        forces_final['stop'] = max(force_limits['stop'])
        return forces_final

    # calculate COG
    def defuzzify(self, x, y):
        num = 0.0  # numerator
        den = 0.0  # denominator
        for i in xrange(len(x)):
            num += y[i] * x[i] * self.dt
            den += y[i] * self.dt
        if den == 0.0:
            return 0.0
        return num / float(den)

    def decide(self, world):
        output = self._make_output()
        inputs = self._make_input(world)
        force_dict = self.inference(inputs['pa'], inputs['pv'])
        x = np.arange(-100, 100 + self.dt, self.dt)
        force = np.zeros(len(x))
        for i in xrange(len(x)):
            force[i] = max(
                min(self.force_stop(x[i]), force_dict['stop']),
                min(self.force_left_fast(x[i]), force_dict['left_fast']),
                min(self.force_left_slow(x[i]), force_dict['left_slow']),
                min(self.force_right_fast(x[i]), force_dict['right_fast']),
                min(self.force_right_slow(x[i]), force_dict['right_slow'])
            )
        output['force'] = self.defuzzify(x, force)
        return output['force']
