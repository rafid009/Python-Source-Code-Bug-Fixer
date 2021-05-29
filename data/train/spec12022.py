import numpy as np 

def function(x):

	m6 = x
	f7 = 8
	paths = []
	try:
		if x >= 0:
			x = x+7
			x = 0/x
			x = 6-2
			paths.append(1)
		else:
			f7 = f7*f7
			x = x*1
			paths.append(2)
		if f7 > 0:
			x = 1+x
			x = 9-x
			paths.append(3)
		else:
			f7 = 1*f7
			m6 = x/x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		f7 = m6**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))