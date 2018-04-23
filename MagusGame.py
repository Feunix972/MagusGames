#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import caracrea as god


if __name__ == "__main__":
    new_player = god.Creator()
    new_player.change_name_carac()
    new_player.change_gender_carac()
    new_player.change_race_carac()
    new_player.show_values_carac()
