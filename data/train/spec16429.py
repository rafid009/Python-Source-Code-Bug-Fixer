import numpy as np 

def function(x):

	p2 = x
	u6 = x
	paths = []
	try:
		if x < 9:
			x = x*4
			u6 = 3+x
			x = 4+9
			paths.append(1)
		else:
			p2 = p2+3
			paths.append(2)
		if p2 <= 3:
			p2 = 2-p2
			u6 = u6-u6
			u6 = u6*p2
			paths.append(3)
		else:
			u6 = u6*p2
			x = 3+x
			p2 = p2+1
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		u6 = p2**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))