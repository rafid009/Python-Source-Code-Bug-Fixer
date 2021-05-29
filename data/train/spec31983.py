import numpy as np 

def function(x):

	m0 = x
	v6 = x
	paths = []
	try:
		if v6 <= 7:
			x = 3+m0
			paths.append(1)
		else:
			x = x+m0
			v6 = 2*6
			x = 5/5
			paths.append(2)
		if x <= 8:
			v6 = v6-x
			m0 = m0-m0
			v6 = v6+x
			paths.append(3)
		else:
			v6 = x*v6
			m0 = m0+7
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))