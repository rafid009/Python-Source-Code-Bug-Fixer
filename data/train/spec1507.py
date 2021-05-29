import numpy as np 

def function(x):

	p0 = 5
	j1 = x
	paths = []
	try:
		if x >= 5:
			x = 2*x
			p0 = p0/2
			x = x+1
			paths.append(1)
		else:
			p0 = p0/x
			j1 = 3*9
			j1 = 6+4
			paths.append(2)
		if j1 <= 3:
			p0 = p0*p0
			j1 = j1/8
			x = x*0
			paths.append(3)
		else:
			j1 = j1+7
			x = p0+x
			j1 = 7*j1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))