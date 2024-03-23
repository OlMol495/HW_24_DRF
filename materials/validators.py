from rest_framework.exceptions import ValidationError


class ValidateVideoLink():
    """ Проверка на публикацию ссылок на видео только с youtube """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = 'https://www.youtube.com/'
        tmp_val = dict(value).get(self.field)
        if not tmp_val.startswith(link):
            raise ValidationError('Допускаются ссылки только на видео с youtube')
        # if link not in tmp_val:
        #     raise ValidationError('Допускаются ссылки только на видео с youtube')
