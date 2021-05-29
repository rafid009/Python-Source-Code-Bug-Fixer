import numpy as np 

def function(x):

	f1 = x
	m7 = 7
	paths = []
	try:
		if x > 6:
			x = x-5
			x = x+3
			f1 = 4-f1
			paths.append(1)
		else:
			m7 = m7-2
			x = 5/5
			x = 3/m7
			paths.append(2)
		if x <= 8:
			f1 = x*8
			paths.append(3)
		else:
			f1 = 9/f1
			m7 = f1*4
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		f1 = m7**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))