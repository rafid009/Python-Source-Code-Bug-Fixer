import numpy as np 

def function(x):

	p7 = 9
	j2 = 1
	paths = []
	try:
		if p7 > 7:
			x = x*x
			j2 = 4-5
			p7 = p7/8
			paths.append(1)
		else:
			p7 = 3+p7
			x = x+5
			p7 = 8+8
			paths.append(2)
		if x <= 8:
			p7 = 1+9
			p7 = 8/x
			paths.append(3)
		else:
			j2 = 6+j2
			p7 = 9-p7
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