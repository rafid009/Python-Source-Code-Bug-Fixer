import numpy as np 

def function(x):

	m0 = x
	f7 = x
	x = 8
	paths = []
	try:
		if x < 3:
			f7 = 7/f7
			f7 = f7/6
			x = x/7
			paths.append(1)
		else:
			x = f7*x
			x = 9*m0
			paths.append(2)
		if f7 < 9:
			f7 = x+9
			f7 = f7-2
			x = 2-1
			paths.append(3)
		else:
			m0 = 3/f7
			f7 = 7-2
			f7 = 5+f7
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		f7 = m0**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))