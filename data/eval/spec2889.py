import numpy as np 

def function(x):

	m7 = 7
	v3 = x
	paths = []
	try:
		if v3 <= 2:
			x = x*3
			m7 = m7-1
			m7 = 7*8
			paths.append(1)
		else:
			m7 = x/m7
			x = 2/x
			paths.append(2)
		if v3 <= 5:
			x = v3+x
			x = 9/x
			x = x*8
			paths.append(3)
		else:
			m7 = 3+5
			m7 = m7-9
			m7 = m7+9
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))