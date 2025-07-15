#uses json library to package data
import json

#uses zipfile and base64 to read the zip file
import zipfile
import base64

import io
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
import logging

#set up logger info
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class zipResponseParser:
    def __init__(self, base_output_dir: str = "extracted_data"):
        self.base_output_dir = Path(base_output_dir)
        self.base_output_dir.mkdir(exist_ok=True)
    
def parse_zip_response(self, response_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse ZIP response and extract JSON files
        
        Args:
            response_data: The JSON response containing ZIP data
            
        Returns:
            Dictionary containing extraction results
        """
        if response_data.get("status") != "OK":
            raise ValueError(f"Response status is not OK twin: {response_data.get('status')}")
            
        dataset = response_data.get("dataset", {})
        zip_b64 = dataset.get("zip")
        
        if not zip_b64:
            raise ValueError("No ZIP data found in response")
            
        # Create session-specific directory
        session_name = dataset.get("session_name", "unknown_session")
        session_dir = self.base_output_dir / self._sanitize_filename(session_name)
        session_dir.mkdir(exist_ok=True)
        
        # Decode base64 ZIP data
        try:
            zip_binary = base64.b64decode(zip_b64)
        except Exception as e:
            raise ValueError(f"Failed to decode base64 ZIP data: {e}")
            
        # Extract files from ZIP
        extraction_results = self._extract_zip_files(
            zip_binary, session_dir, dataset
        )
        
        return {
            "status": "success",
            "session_info": {
                "session_id": dataset.get("session_id"),
                "session_name": session_name,
                "dataset_hash": dataset.get("dataset_hash"),
                "dataset_date": dataset.get("dataset_date"),
                "dataset_size": dataset.get("dataset_size")
            },
            "extraction_results": extraction_results,
            "output_directory": str(session_dir)
        }
    

