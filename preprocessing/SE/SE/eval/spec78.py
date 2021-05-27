import numpy as np 

def function(x):

	u3 = x
	p2 = x
	paths = []
	try:
		if p2 >= 4:
			p2 = p2+9
			x = 3/8
			paths.append(1)
		else:
			x = x+8
			p2 = x*p2
			x = x/9
			paths.append(2)
		if p2 > 3:
			u3 = u3+x
			p2 = p2+2
			x = x*3
			paths.append(3)
		else:
			p2 = 3-x
			u3 = 8*x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		p2 = u3**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))