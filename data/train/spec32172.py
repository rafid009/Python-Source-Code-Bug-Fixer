import numpy as np 

def function(x):

	p5 = x
	k1 = x
	paths = []
	try:
		if p5 < 4:
			k1 = 0*k1
			x = 7+9
			paths.append(1)
		else:
			p5 = k1-p5
			p5 = p5+8
			paths.append(2)
		if x > 2:
			x = 6*p5
			k1 = 2-k1
			x = x-1
			paths.append(3)
		else:
			k1 = 2+k1
			x = x/p5
			x = x+2
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))