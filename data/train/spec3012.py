import numpy as np 

def function(x):

	f1 = x
	p6 = x
	x = x
	paths = []
	try:
		if f1 >= 2:
			p6 = p6*6
			paths.append(1)
		else:
			p6 = p6*6
			x = x-1
			paths.append(2)
		if x > 4:
			x = x*8
			f1 = f1+9
			paths.append(3)
		else:
			f1 = p6+f1
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		f1 = p6**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))