import numpy as np 

def function(x):

	h6 = 0
	j2 = x
	x = 7
	paths = []
	try:
		if x <= 4:
			j2 = j2*x
			x = h6-9
			h6 = j2/h6
			paths.append(1)
		else:
			x = x/4
			h6 = j2-x
			j2 = j2-x
			paths.append(2)
		if j2 >= 8:
			j2 = j2+2
			j2 = j2*0
			h6 = h6*4
			paths.append(3)
		else:
			j2 = j2-7
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))