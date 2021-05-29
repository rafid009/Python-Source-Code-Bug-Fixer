import numpy as np 

def function(x):

	m5 = 6
	i6 = 1
	paths = []
	try:
		if i6 < 8:
			m5 = 4/x
			paths.append(1)
		else:
			i6 = i6/7
			x = 8+x
			paths.append(2)
		if m5 >= 9:
			m5 = m5*0
			i6 = 6+x
			paths.append(3)
		else:
			m5 = 3-2
			m5 = 7*m5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))