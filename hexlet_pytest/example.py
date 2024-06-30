class MultiKeyDict(object):
    """Словареподобный контейнер, позволяющий иметь псевдонимы ключей."""

    def __init__(self, **kwargs):
        """
        Инициализирует контейнер.

        Arguments:
            kwargs — пары "ключ-значение", которые будет содержать
            контейнер сразу после инициализации.

        """
        # BEGIN (write your solution here)
        
        # END

    def __getitem__(self, key):
        """
        Возвращает значение по ключу.

        Arguments:
        - key — один из ключей, связанных со значением.

        """
        # BEGIN (write your solution here)
        
        # END

    def __setitem__(self, key, value):
        """
        Сохраняет значение по указанному ключу.

        Изменение затрагивает все псевдонимы ключа. Любой из псевдонимов
        может быть указан в роли ключа.

        Arguments:
            key — ключ, по которому будет сохранено значение,
            value — сохраняемое по указанному ключу значение.

        """
        # BEGIN (write your solution here)
        
        # END

    def alias(self, **kwargs):
        """
        Добавляет псевдоним(ы) для существующих ключей.

        Arguments:
            kwargs — пары "новый ключ - старый ключ". Все "старые ключи"
            должны уже присутствовать в контейнере.

        """
        # BEGIN (write your solution here)
        
        # END
