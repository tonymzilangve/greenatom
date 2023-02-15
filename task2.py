from typing import List, Callable, Any


def callback(num: int) -> int:
    return num * 5


def create_handlers(callback: Callable[[int], Any]) -> List[Callable[[int], Any]]:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step))
    return handlers


def execute_handlers(handlers: List[Callable[[int], Any]]) -> None:
    # запускаем добавленные обработчики(шаги от 0 до 4)
    for handler in handlers:
        print(handler())


if __name__ == '__main__':
    execute_handlers(create_handlers(callback))
