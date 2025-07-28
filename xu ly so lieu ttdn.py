# Xử lý số liệu tổn thất

import pandas as pd

ttdn = pd.read_excel (r'D:\thai\table5.xlsx')

print(ttdn)

ttdn.head(13)

ttdn.shape

solieu1 = pd.DataFrame(ttdn, columns=['Điện lực', 'So sánh cùng kỳ'])

# Bỏ dòng "Tổng cộng"
solieux = solieu1[solieu1['Điện lực'] != 'Tổng cộng'].copy()

print(solieux)

# Làm tròn
solieux['So sánh cùng kỳ'] = solieux['So sánh cùng kỳ'].round(2)

# Nhóm tăng/giảm
giamx = solieux[solieux['So sánh cùng kỳ'] < 0]
tangx = solieux[solieux['So sánh cùng kỳ'] > 0]

# Mô tả từng nhóm
giam_str1 = ', '.join([f"{row['Điện lực']} ({row['So sánh cùng kỳ']:.2f})" for _, row in giamx.iterrows()])
tang_str1 = ', '.join([f"{row['Điện lực']} ({row['So sánh cùng kỳ']:.2f})" for _, row in tangx.iterrows()])

# Ghép mô tả đầy đủ
ket_qua_1 = f"""Tổn thất giảm so với cùng kỳ gồm: {giam_str1}.
Tổn thất tăng so với cùng kỳ gồm: {tang_str1}."""

print(ket_qua_1)


solieu2 = pd.DataFrame(ttdn, columns=['Điện lực', 'So sánh KH'])
#print(solieu2)

solieuy = solieu2[solieu2['Điện lực'] != 'Tổng cộng'].copy()

print(solieuy)

# Làm tròn
solieuy['So sánh KH'] = solieuy['So sánh KH'].round(2)

# Nhóm tăng/giảm
giamy = solieuy[solieuy['So sánh KH'] < 0]
tangy = solieuy[solieuy['So sánh KH'] > 0]

# Mô tả từng nhóm
giam_str2 = ', '.join([f"{row['Điện lực']} ({row['So sánh KH']:.2f})" for _, row in giamy.iterrows()])
tang_str2 = ', '.join([f"{row['Điện lực']} ({row['So sánh KH']:.2f})" for _, row in tangy.iterrows()])

# Ghép mô tả đầy đủ
ket_qua_2 = f"""Tổn thất giảm so với cùng kỳ gồm: {giam_str2}. Tổn thất tăng so với cùng kỳ gồm: {tang_str2}."""

print(ket_qua_2)



