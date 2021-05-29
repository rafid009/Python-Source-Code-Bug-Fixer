import numpy as np 

def function(x):

	j8 = x
	m5 = x
	paths = []
	try:
		if j8 > 4:
			x = x/x
			m5 = 0-9
			paths.append(1)
		else:
			x = x-3
			x = 3+m5
			m5 = m5-j8
			paths.append(2)
		if x <= 3:
			x = x*0
			m5 = 2*m5
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		j8 = m5**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))