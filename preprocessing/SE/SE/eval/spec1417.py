import numpy as np 

def function(x):

	w5 = x
	b6 = 6
	x = x
	paths = []
	try:
		if b6 < 1:
			w5 = 2+w5
			b6 = b6+5
			paths.append(1)
		else:
			w5 = 4/3
			paths.append(2)
		if w5 <= 4:
			x = 9-x
			w5 = 7*x
			x = 2-x
			paths.append(3)
		else:
			b6 = 7*b6
			b6 = b6*0
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		b6 = w5**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))