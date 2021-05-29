import numpy as np 

def function(x):

	w5 = 4
	m9 = 8
	paths = []
	try:
		if x <= 5:
			x = x/m9
			m9 = 5-0
			m9 = 1/w5
			paths.append(1)
		else:
			m9 = 1-m9
			paths.append(2)
		if w5 >= 9:
			x = 2*x
			x = 6+9
			x = 3*x
			paths.append(3)
		else:
			x = 2+x
			x = x/2
			x = w5*3
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))