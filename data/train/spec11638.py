import numpy as np 

def function(x):

	w8 = 6
	m1 = x
	x = 9
	paths = []
	try:
		if m1 <= 3:
			w8 = 6-4
			x = 1/x
			w8 = w8+m1
			paths.append(1)
		else:
			w8 = w8*9
			w8 = w8+w8
			paths.append(2)
		if w8 <= 6:
			m1 = 6/3
			x = x*0
			paths.append(3)
		else:
			w8 = 1+w8
			x = m1*w8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		m1 = w8**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))