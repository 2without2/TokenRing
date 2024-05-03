# Лабораторная работа №5

## Задание

1. Взять за основу программу, относящуюся к лабораторной работе №3.
2. Программа должна соответствовать однонаправленной кольцевой топологии, охватывающей три пользовательские станции.
3. Программа должна включать по крайней мере две подпрограммы -- передающую и принимающую, если задействуются реальные COM-порты. Либо три пары таковых подпрограмм, если пользовательские станции эмулируются.
4. К каждой станции должны относиться отдельные окна для ввода и вывода текстовых сообщений.
5. На станции-передатчике сообщение должно разбиваться на блоки фиксированной длины. Поскольку алгоритм Token Ring не мыслим без дополнительных служебных полей, блоки должны "обрамляться" этими полями.
6. Для обеспечения возможности выбора станции назначения должна быть предусмотрена юникаст-адресация (дополнительные элементы интерфейса для присвоения и указания адресов, одно либо несколько соответствующих полей в структуре пакета).
7. Должны быть предусмотрены два уровня приоритетов станций (дополнительные элементы интерфейса для присвоения приоритетов, одно либо несколько соответствующих полей в структуре пакета).
8. Должна быть реализована суть алгоритма Token Ring: перепасовка маркера и использование маркера для пересылки сообщения с учетом приоритетов. Остальное (например, раннее освобождение маркера) -- опционально.
9. Любая из станций по требованию должна становиться и станцией-монитором -- в дополнение к своему основному назначению. Минимальный набор функций станции-монитора: генерация маркера, контроль маркера, предотвращение циклов.
10. Программа должна иметь отдельное отладочное окно. В этом окне, по крайней мере, должно отражаться продвижение маркера и пакетов с данными.
11. Программа должна работать "циклически".
