import numpy as np 

def function(x):

	i5 = x
	m9 = x
	paths = []
	try:
		if x >= 2:
			m9 = 2-4
			x = 6+7
			paths.append(1)
		else:
			x = x*0
			i5 = i5/4
			paths.append(2)
		if m9 > 1:
			i5 = x-m9
			x = i5*2
			paths.append(3)
		else:
			x = 8-7
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))