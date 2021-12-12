basic.show_number(1)
basic.show_number(2)
basic.show_number(3)
basic.show_number(4)
basic.show_number(5)
basic.show_leds("""
    . . # . .
    . . # . .
    # . # . #
    . # # # .
    . . # . .
    """)
basic.show_string("Hello!")
basic.show_icon(IconNames.HEART)
basic.show_arrow(ArrowNames.NORTH_EAST)
basic.show_arrow(ArrowNames.SOUTH_EAST)
basic.show_arrow(ArrowNames.SOUTH_WEST)
basic.show_arrow(ArrowNames.NORTH_WEST)
basic.clear_screen()
basic.pause(500)