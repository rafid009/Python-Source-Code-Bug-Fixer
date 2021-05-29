import numpy as np 

def function(x):

	i2 = x
	m5 = 9
	paths = []
	try:
		if i2 <= 1:
			m5 = 3-m5
			m5 = x/6
			paths.append(1)
		else:
			i2 = i2*i2
			paths.append(2)
		if x <= 3:
			i2 = 9/x
			x = x/x
			x = x+5
			paths.append(3)
		else:
			i2 = 3+5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		i2 = m5**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))