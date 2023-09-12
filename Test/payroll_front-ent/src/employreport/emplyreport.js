import React, { useState } from 'react';
import Papa from 'papaparse';

function EmployeeReport() {
    const [formdata, setFormdata] = useState({});
    const [report, setReport] = useState([]);
    const [loading, setLoading] = useState(false);
    const [report_id, setReportId] = useState(false);
    const handleFileUpload = (event) => {
        const formObj = {};

        const file = event.target.files[0];
        formObj['file_name'] = file.name;

        console.log(file)
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const csvData = e.target.result;
                Papa.parse(csvData, {
                    header: true,
                    dynamicTyping: true,
                    complete:(result) => {
                        formObj['data'] = result.data;
                    },
                    error: (error) => {
                        console.error('error while pursing csv file')
                    }
                })
            }
            reader.readAsText(file);
        }
        setFormdata(formObj)
    }

    const handleGetReport = () => {
        setLoading(true)
        const apiUrl = "http://127.0.0.1:8001/api/get-report/?report_id=" + report_id
        fetch(apiUrl)
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                console.log(data)
                setLoading(false)
                
            })
            .catch((error) => {
                console.log(error)
                alert(error)
                setLoading(false)
            });
    }
    const handleButtonSubmit = () => {
        setLoading(true)
        fetch('http://127.0.0.1:8001/api/create-employee-report/', {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
            },
            body: JSON.stringify(formdata)
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("${response.status}")
                }
                return response.json()
            })
            .then((data) => {
                console.log(data)
                setLoading(false)
                setReport(data.payrollReport)
                alert(data.message)
            })
            .catch((error) => {
                console.log(error)
                alert(error)
                setLoading(false)
            })
    }
    return (

        <div className="employee-report" style={{ display: "flex", flexDirection: "column", paddingInline: "15%", background: "#e1ddde", paddingBottom: "40px", margin:"10$" }}>
            <h1>Pay roll system</h1>
            <div style={{ display: "flex", flexDirection: "row" }} className="container">
            <div style={{ display: "flex", flexDirection: "row", justifyContent: "flex-start" }} >
                    <div style={{ fontSize: 14, fontWeight:"500" }}>Upload file:</div>
                    <div>
                        <input type="file" accept=".csv" onChange={(e) => {handleFileUpload(e)}}/>
                    </div>
                </div>
                <div style={{ justifyContent: "flex-end" }}>
                    <button  className="submit" onClick={() => handleButtonSubmit()}>Submit</button>
                </div>
            </div>
            <div style={{ display: "flex", flexDirection: "row" }} className="container">
                <div style={{ display: "flex", flexDirection: "row",justifyContent: "flex-start" }} >
                    <div style={{ fontSize: 14, fontWeight: "500" }}>Get report:</div>
                    <div>
                        <input type="text" placeholder="Report id" onChange={(e) => { setReportId(e.target.value) }} />
                    </div>
                </div>
                <div style={{ justifyContent: "flex-end" }}>
                    <button className="submit" onClick={() => handleGetReport()}>Fetch report</button>
                </div>
            </div>
        </div>
        
        );
}
export default EmployeeReport;