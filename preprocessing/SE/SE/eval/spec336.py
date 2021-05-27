import numpy as np 

def function(x):

	t6 = x
	p0 = 4
	paths = []
	try:
		if p0 >= 8:
			x = x/p0
			p0 = p0*3
			paths.append(1)
		else:
			t6 = 4*0
			t6 = t6-6
			p0 = p0*0
			paths.append(2)
		if p0 <= 2:
			p0 = x+p0
			p0 = p0/t6
			paths.append(3)
		else:
			x = 0*x
			t6 = t6+0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))