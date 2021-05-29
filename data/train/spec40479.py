import numpy as np 

def function(x):

	j2 = 2
	p5 = 5
	paths = []
	try:
		if j2 < 2:
			x = 8-x
			paths.append(1)
		else:
			j2 = j2*1
			j2 = x+j2
			paths.append(2)
		if j2 < 8:
			x = 4*5
			p5 = 1*x
			x = 0-x
			paths.append(3)
		else:
			x = x*4
			j2 = j2+1
			x = p5/x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))