import numpy as np 

def function(x):

	m3 = x
	v5 = 7
	paths = []
	try:
		if v5 >= 5:
			v5 = 1*m3
			v5 = v5*v5
			x = x/9
			paths.append(1)
		else:
			v5 = m3*2
			x = x+1
			paths.append(2)
		if x >= 6:
			v5 = v5/6
			m3 = m3-6
			paths.append(3)
		else:
			v5 = 7+v5
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		v5 = m3**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))