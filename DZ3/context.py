from contextlib import contextmanager
# # Контексный менеджер (генератор текста)
""" Пример """
# with open('txt_v1.txt') as txt:
#     for init in txt.read().split(', '):
#         print('Test #{} of 10'.format(init))


""" Создание """
@contextmanager
def file_open(path, flag):
    try:
        f_object = open(path, flag)
        yield f_object  # Возвращение объекта
    except OSError:
        print("Файл не доступен!")
    finally:
        f_object.close()


if __name__ == '__main__':
    with file_open('txt_v1.txt', 'r') as txt:
        for init in txt.read().split(', '):
            print('Test #{} of 10'.format(init))
