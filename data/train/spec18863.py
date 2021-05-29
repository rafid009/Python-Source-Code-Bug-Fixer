import numpy as np 

def function(x):

	j3 = 9
	p9 = 9
	paths = []
	try:
		if j3 < 2:
			x = j3*2
			j3 = 1/1
			paths.append(1)
		else:
			j3 = j3-6
			x = x*p9
			j3 = 4-j3
			paths.append(2)
		if x <= 3:
			x = x*8
			j3 = x/7
			paths.append(3)
		else:
			x = j3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))