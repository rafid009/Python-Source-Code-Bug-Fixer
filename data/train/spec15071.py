import numpy as np 

def function(x):

	m5 = 2
	i8 = 7
	x = x
	paths = []
	try:
		if x <= 8:
			x = x*7
			m5 = m5*x
			m5 = 1-x
			paths.append(1)
		else:
			i8 = i8/6
			paths.append(2)
		if i8 >= 7:
			x = x*3
			i8 = i8*i8
			paths.append(3)
		else:
			x = 5*8
			i8 = m5+m5
			m5 = m5-1
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		i8 = m5**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))