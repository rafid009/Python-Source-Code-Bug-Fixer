import numpy as np 

def function(x):

	p6 = 3
	f5 = x
	paths = []
	try:
		if p6 >= 0:
			x = 5/x
			p6 = p6*6
			x = f5/6
			paths.append(1)
		else:
			p6 = 3-1
			paths.append(2)
		if x > 4:
			p6 = 8*p6
			f5 = 1/6
			f5 = f5+f5
			paths.append(3)
		else:
			p6 = 1-6
			p6 = p6*2
			f5 = 4-f5
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))