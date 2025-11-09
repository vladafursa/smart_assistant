import { useRef, useState } from 'react'

const DropBox = () => {
  const uploadRef = useRef(null)  
  const [file, setFile] = useState(null)
  const [isDragOver, setIsDragOver] = useState(false)

  const handleChange = () => {
    setFile(uploadRef.current.files[0])
  }

  const handleDragOver = (e) => {
    e.preventDefault()
    setIsDragOver(true)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    setIsDragOver(false)   // reset when dropped
    // you could also read e.dataTransfer.files here
  }

  return (
    <div className="mx-auto max-w-3xl p-6">
      <div
        className={`mt-4 rounded-lg border-2 border-dashed border-gray-300 p-12 text-center cursor-pointer transition 
          hover:border-blue-500 hover:bg-blue-50 
          ${isDragOver ? 'opacity-50 border-blue-500 bg-blue-50' : ''}`}
        onClick={() => uploadRef.current.click()}
        onDragOver={handleDragOver}
        onDrop={handleDrop}
        onDragLeave={() => setIsDragOver(false)}
      >
        {/* icon */}
        <svg
          className="mx-auto h-12 w-12 text-gray-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeWidth="2"
            d="M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2M16 12l-4-4m0 0l-4 4m4-4v12"
          />
        </svg>

        <input
          ref={uploadRef}
          type="file"
          style={{ display: 'none' }}
          onChange={handleChange}
        />
      </div>

      <p>{file && file.name}</p>
    </div>
  )
}

export default DropBox
