from itertools import permutations

def encrypt(text, block_size, permutation):
    """
    Шифрует текст блочным методом с использованием заданной перестановки.
    
    Аргументы:
    text -- исходный текст для шифрования
    block_size -- длина блока (n)
    permutation -- кортеж/список перестановки длины n (позиции с 1 до n)
    
    Возвращает:
    Зашифрованный текст.
    """
    # Дополняем текст пробелами, если последний блок неполный
    if len(text) % block_size != 0:
        text += " " * (block_size - len(text) % block_size)
    
    encrypted_text = ""
    # Обрабатываем текст блоками
    for i in range(0, len(text), block_size):
        block = text[i:i+block_size]
        # Создаём список для зашифрованного блока
        encrypted_block = [''] * block_size
        # Для каждого символа исходного блока определяем его позицию по ключу
        for idx, char in enumerate(block):
            target_position = permutation[idx] - 1  # перевод в 0-индексацию
            encrypted_block[target_position] = char
        encrypted_text += "".join(encrypted_block)
    return encrypted_text

def decrypt(ciphertext, block_size, permutation):
    """
    Расшифровывает текст блочным методом, используя ключ-перестановку.
    
    Аргументы:
    ciphertext -- зашифрованный текст
    block_size -- длина блока (n)
    permutation -- кортеж/список перестановки, использованный для шифрования
    
    Возвращает:
    Расшифрованный (исходный) текст.
    """
    # Вычисляем обратную перестановку.
    # Если permutation[i] = j, то обратная перестановка в позиции j-1 равна i+1
    inverse_perm = [0] * block_size
    for i, pos in enumerate(permutation):
        inverse_perm[pos - 1] = i + 1

    decrypted_text = ""
    # Обрабатываем зашифрованный текст блоками
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted_block = [''] * block_size
        # Восстанавливаем порядок символов с помощью обратной перестановки
        for j, char in enumerate(block):
            original_index = inverse_perm[j] - 1
            decrypted_block[original_index] = char
        decrypted_text += "".join(decrypted_block)
    return decrypted_text

def brute_force_decrypt(ciphertext, block_size):
    """
    Перебором подбирает ключ для расшифровки ciphertext, если ключ неизвестен.
    Для каждого варианта перестановки выводит ключ и полученный вариант расшифровки.
    """
    # Генерируем все перестановки чисел от 1 до block_size (всего block_size! вариантов)
    for key in permutations(range(1, block_size + 1)):
        decrypted = decrypt(ciphertext, block_size, key)
        print("Ключ:", key, "->", decrypted)

if __name__ == "__main__":
    # Зашифрованный текст, для которого неизвестен ключ, блоки имеют длину 6
    ciphertext = " втоХякоее  ныевснглв хз яадяхалич т-ттч окод оипои е итзодроеьлентях ,ое  в екеылубо ыб лтоотч-прен оенедел неон,кот оаил авседп ардеебуж пйин:льваринойын елс свя ем на;у смоо я виларбзо ч ,тл шаневутеГеьоиМ нэт,ун ичп орволдуиздс ео еинаеем огнгокцеобров оияежани - , о,чотндуем ж бми имнолы схого васдот жт :естб еыпееыр дыхеровето  йшчилабеоге ойопск квтсанооп лпон йеноивдж титс, зж ееочагадрееын те,ич преж  , кжыиннртсаес еып  .ин"
    block_size = 6
    
    # Перебираем все возможные ключи и выводим варианты расшифровки
    brute_force_decrypt(ciphertext, block_size)
