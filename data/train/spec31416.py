import numpy as np 

def function(x):

	f7 = x
	p0 = x
	paths = []
	try:
		if x <= 4:
			p0 = 2-p0
			x = 3+x
			x = x/6
			paths.append(1)
		else:
			x = 7-x
			x = x*p0
			paths.append(2)
		if x <= 7:
			x = x+x
			f7 = x+1
			paths.append(3)
		else:
			p0 = p0*p0
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))