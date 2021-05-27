import numpy as np 

def function(x):

	p0 = x
	f1 = 1
	paths = []
	try:
		if x > 7:
			x = x/f1
			f1 = x/3
			f1 = x+f1
			paths.append(1)
		else:
			p0 = 3-p0
			p0 = p0/7
			f1 = x-p0
			paths.append(2)
		if f1 >= 9:
			x = 7*f1
			p0 = p0-7
			paths.append(3)
		else:
			f1 = p0+x
			f1 = 6+f1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))