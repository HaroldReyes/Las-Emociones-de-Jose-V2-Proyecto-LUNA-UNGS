def text_objects(text, font):
    textSurface = font.render(text, True, NEGRO)
    return textSurface, textSurface.get_rect()