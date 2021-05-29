import numpy as np 

def function(x):

	j2 = 3
	p9 = x
	paths = []
	try:
		if p9 > 8:
			p9 = p9+5
			x = x*8
			j2 = 4/5
			paths.append(1)
		else:
			p9 = x*0
			x = x*p9
			paths.append(2)
		if x <= 4:
			j2 = j2*0
			paths.append(3)
		else:
			x = 7-x
			j2 = j2+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))